using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace call_data_microcervice.DTO
{
    public class CallDataEntity
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int CallId { get; set; }

        public int ClientId { get; set; }

        public int OperatorId { get; set; }

        public float CallSessionTime { get; set; }
    }
}
