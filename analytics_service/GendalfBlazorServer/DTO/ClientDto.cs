using System.Text.Json.Serialization;

namespace GendalfBlazorServer.DTO
{
    public record ClientDto(
    [property: JsonPropertyName("client_id")] int ClientId,
    [property: JsonPropertyName("name")] string ClientName,
    [property: JsonPropertyName("surname")] string ClientSurname,
    [property: JsonPropertyName("online")] bool Online
);
}
