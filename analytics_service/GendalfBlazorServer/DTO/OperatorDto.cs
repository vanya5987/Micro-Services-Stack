using System.Text.Json.Serialization;

namespace GendalfBlazorServer.DTO
{
    public record OperatorDto(
    [property: JsonPropertyName("operator_id")] int OperatorId,
    [property: JsonPropertyName("name")] string OperatorName,
    [property: JsonPropertyName("surname")] string OperatorSurname,
    [property: JsonPropertyName("online")] bool Online,
    [property: JsonPropertyName("operator_is_busy")] bool OperatorIsBusy
);
}
