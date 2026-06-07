using System.Text.Json.Serialization;

namespace call_data_microcervice.DTO
{
    public record CallDataDto
    (
        [property: JsonPropertyName("client_id")] int ClientId,
        [property: JsonPropertyName("operator_id")] int OperatorId,
        [property: JsonPropertyName("call_session_time")] float CallSessionTime
    );
}
