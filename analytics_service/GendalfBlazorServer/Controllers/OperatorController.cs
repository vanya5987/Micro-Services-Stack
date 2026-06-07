using GendalfBlazorServer.DTO;
using Microsoft.AspNetCore.Mvc;

namespace GendalfBlazorServer.Services
{
    [ApiController]
    [Route("api/analytics-operators")]
    public class OperatorController : ControllerBase
    {
        private readonly HttpClient _http;
        private readonly string _pythonUrl;

        public OperatorController(HttpClient http, IConfiguration configuration)
        {
            _http = http ?? throw new ArgumentNullException(nameof(http));
            _pythonUrl = configuration["PythonServices:OperatorsUrl"]
                ?? throw new InvalidOperationException();
        }

        [HttpGet]
        public async Task<IActionResult> GetOperators()
        {
            var data = await _http.GetFromJsonAsync<List<OperatorDto>>(_pythonUrl) ?? new();
            return Ok(data);
        }

        [HttpPost]
        public async Task<IActionResult> CreateOperator([FromBody] OperatorDto operatorDto)
        {
            var url = _pythonUrl.EndsWith("/") ? _pythonUrl : $"{_pythonUrl}/";
            await _http.PostAsJsonAsync(url, operatorDto);
            return Ok();
        }
    }
}