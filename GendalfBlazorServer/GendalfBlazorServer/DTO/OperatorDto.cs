using System.Text.Json.Serialization;

namespace GendalfBlazorServer.DTO
{
    public class OperatorDto
    {
        [JsonPropertyName("operator_id")]
        public int OperatorId { get; set; }

        [JsonPropertyName("name")]
        public string OperatorName { get; set; } = "";

        [JsonPropertyName("surname")]
        public string OperatorSurname { get; set; } = "";

        [JsonPropertyName("online")]
        public bool Online { get; set; }

        [JsonPropertyName("operator_is_busy")]
        public bool OperatorIsBusy { get; set; }
    }
}
