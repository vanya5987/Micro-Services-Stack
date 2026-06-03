using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using GendalfPractice.Data;
using GendalfPractice.Model;

namespace GendalfPractice.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ClientController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public ClientController(ApplicationDbContext context)
        {
            _context = context ?? throw new ArgumentNullException(nameof(context));
        }

        [HttpGet]
        public async Task<IActionResult> GetAll()
        {
            var clients = await _context.Clients
                .AsNoTracking()
                .ToListAsync();

            return Ok(clients);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetClientById(long id)
        {
            var clients = await _context.Clients
                .AsNoTracking().
                FirstOrDefaultAsync(client => client.Id == id);

            if (clients == null)
                return NotFound();

            return Ok(clients);
        }

        [HttpPost]
        public async Task<IActionResult> CreateClient([FromBody] Client client)
        {
            _context.Clients.Add(client);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetClientById), new { id = client.Id }, client);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateClient([FromBody]Client clientDto, int id)
        {
            var exeistClient = await _context.Clients.FirstOrDefaultAsync(client => client.Id == id);

            if (exeistClient == null)
                return NotFound();

            exeistClient.Name = clientDto.Name;
            exeistClient.Surname = clientDto.Surname;
            exeistClient.Salary = clientDto.Salary;

            await _context.SaveChangesAsync();

            return NoContent();
        }
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteClient()
        {
            return NoContent();
        }
    }
}
