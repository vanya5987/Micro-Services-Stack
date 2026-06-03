using Microsoft.EntityFrameworkCore;
using GendalfPractice.Data;

//Отличие структуры от класса? - ОТРАБОТАНО
//Stack/Heap - ОТРАБОТАНО
//GC - ОТРАБОТАНО
//Ref/out/in - ОТРАБОТАНО
//Interfaces/Abstract class - ОТРАБОТАНО
//IEnumerable/ICollection/IList/IQuerable
//Async/Threading/Processes
//Linq
//EfCore
//Migrations (Миграции в продакшене) - ОТРАБОТАНО
//MappingResponse (Automapping)
//OnModelCreating - ОТРАБОТАНО
//Docker
//JavaScript
//Postgres
//Microservices - ОТРАБОТАНО
//Kafka
//Deadlock
//Один ко многим и многие к одному
//FluentApi
//InitTest
//MocTests

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddRazorPages();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

builder.Services.AddDbContextPool<ApplicationDbContext>(options => 
    options.UseNpgsql(connectionString),
    poolSize: 1024
);

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(); // Это как раз интерфейс в браузере
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllers();
app.MapRazorPages();

app.Run();
