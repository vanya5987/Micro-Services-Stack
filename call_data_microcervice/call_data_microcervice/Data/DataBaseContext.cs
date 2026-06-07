using call_data_microcervice.DTO;
using Microsoft.EntityFrameworkCore;

namespace call_data_microcervice.API
{
    public class DataBaseContext : DbContext
    {
        public DataBaseContext(DbContextOptions<DataBaseContext> options) : base(options) { }


        public DbSet<CallDataEntity> CallDataEntity { get; set; }
    }
}
