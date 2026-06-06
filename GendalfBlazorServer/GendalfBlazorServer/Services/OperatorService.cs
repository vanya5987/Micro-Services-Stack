using GendalfBlazorServer.DTO;

namespace GendalfBlazorServer.Services
{
    public class OperatorService
    {
        private readonly HttpClient _http;

        public OperatorService(HttpClient http)
        {
            _http = http ?? throw new ArgumentNullException(nameof(http));
        }

        async public Task<List<OperatorDto>> GetOperators() =>
            await _http.GetFromJsonAsync<List<OperatorDto>>("/operators") ?? new();

        async public Task CreateOperator(OperatorDto newOperator) =>
            await _http.PostAsJsonAsync("/operators/", newOperator);
    }
}
