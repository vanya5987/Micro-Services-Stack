using GendalfBlazorServer.DTO;

namespace GendalfBlazorServer.Services
{
    public class ClientService
    {
        private readonly HttpClient _http;

        public ClientService(HttpClient http)
        {
            _http = http ?? throw new ArgumentNullException(nameof(http));
        }

        async public Task<List<ClientDto>> GetClients() =>
            await _http.GetFromJsonAsync<List<ClientDto>>("/clients") ?? new();

        async public Task CreateClient(ClientDto client) =>
            await _http.PostAsJsonAsync("/clients/", client);
    }
}
