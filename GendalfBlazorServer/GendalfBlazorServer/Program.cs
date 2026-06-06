using GendalfBlazorServer.Data;
using GendalfBlazorServer.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddSingleton<WeatherForecastService>();

builder.Services.AddHttpClient<ClientService>(client =>
    client.BaseAddress = new Uri("http://127.0.0.1:8001")
    );

builder.Services.AddHttpClient<OperatorService>(client =>
    client.BaseAddress = new Uri("http://127.0.0.1:8002")
    );

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
