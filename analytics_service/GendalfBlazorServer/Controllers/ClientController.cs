using GendalfBlazorServer.DTO;
using Microsoft.AspNetCore.Mvc;

namespace GendalfBlazorServer.Services
{
    [ApiController]
    [Route("api/analytics-clients")]
    public class ClientController : ControllerBase
    {
        private readonly HttpClient _http;
        private readonly string _pythonUrl;

        public ClientController(HttpClient http, IConfiguration configuration)
        {
            _http = http ?? throw new ArgumentNullException(nameof(http));
            _pythonUrl = configuration["PythonServices:ClientsUrl"]
                ?? throw new InvalidOperationException();
        }

        [HttpGet]
        public async Task<IActionResult> GetClients()
        {
            var data = await _http.GetFromJsonAsync<List<ClientDto>>(_pythonUrl) ?? new();
            return Ok(data);
        }

        [HttpPost]
        public async Task<IActionResult> CreateClient([FromBody] ClientDto client)
        {
            var url = _pythonUrl.EndsWith("/") ? _pythonUrl : $"{_pythonUrl}/";
            await _http.PostAsJsonAsync(url, client);
            return Ok();
        }
    }
}