using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;

namespace call_data_microcervice.DTO
{
    public class CallDataEntity
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [JsonPropertyName("call_id")]
        public int CallId { get; set; }

        [JsonPropertyName("client_id")]
        public int ClientId { get; set; }

        [JsonPropertyName("operator_id")]
        public int OperatorId { get; set; }

        [JsonPropertyName("call_session_time")]
        public float CallSessionTime { get; set; }

        [JsonPropertyName("call_date")]
        public DateTime CallDate { get; set; }
    }
}
