using System.Text.Json.Serialization;

namespace GendalfBlazorServer.DTO
{
    public class ClientDto
    {
        [JsonPropertyName("client_id")]
        public int ClientId { get; set; }

        [JsonPropertyName("name")]
        public string ClientName { get; set; } = "";

        [JsonPropertyName("surname")]
        public string ClientSurname { get; set; } = "";

        [JsonPropertyName("balance")]
        public int Balance { get; set; }

        [JsonPropertyName("online")]
        public bool Online { get; set; }
    }
}
