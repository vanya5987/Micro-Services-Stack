using call_data_microcervice.API;
using call_data_microcervice.DTO;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace call_data_microcervice.Services
{
    [ApiController]
    [Route("api/[controller]")]
    public class CallDataController : ControllerBase
    {
        private readonly DataBaseContext _context;

        public CallDataController(DataBaseContext context)
        {
            _context = context ?? throw new ArgumentNullException(nameof(context));
        }

        [HttpPost]
        public async Task<IActionResult> CreateCall([FromBody] CallDataDto call)
        {
            CallDataEntity callData = new CallDataEntity
            {
                ClientId = call.ClientId,
                OperatorId = call.OperatorId,
                CallSessionTime = call.CallSessionTime
            }; 

            _context.CallDataEntity.Add(callData);
            await _context.SaveChangesAsync();

            return Ok(callData);
        }

        [HttpGet]
        public async Task<IActionResult> GetAllCalls()
        {
            var calls = await _context.CallDataEntity
                .OrderBy(call => call.CallId)
                .ToListAsync();

            return Ok(calls);
        }
    }
}
