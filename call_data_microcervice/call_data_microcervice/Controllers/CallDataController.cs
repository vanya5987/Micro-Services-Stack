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

        [HttpPost("create-call")]
        public async Task<IActionResult> CreateCall([FromBody] CallDataDto call)
        {
            CallDataEntity callData = new CallDataEntity
            {
                ClientId = call.ClientId,
                OperatorId = call.OperatorId,
                CallSessionTime = call.CallSessionTime,
                CallDate = DateTime.UtcNow
            }; 

            _context.CallDataEntity.Add(callData);
            await _context.SaveChangesAsync();

            return Ok(callData);
        }

        [HttpGet("all-calls")]
        public async Task<IActionResult> GetAllCalls()
        {
            var calls = await _context.CallDataEntity
                .OrderBy(call => call.CallId)
                .ToListAsync();

            return Ok(calls);
        }

        [HttpGet("operator-stats")]
        public async Task<IActionResult> GetOperatorCallStats(int operatorId)
        {
            var callsTimes = await _context.CallDataEntity
                .Where(call => call.OperatorId == operatorId)
                .Select(call => call.CallSessionTime)
                .ToListAsync();

            if (!callsTimes.Any())
                return NotFound();

            int callsCount = callsTimes.Count();
            float callsAverage = callsTimes.Average();
            float callsSum = callsTimes.Sum();

            return Ok(new OperatorAnalyticsDto(callsCount, callsAverage, callsSum));
        }

        [HttpGet("client-stats")]
        public async Task<IActionResult> GetClientCallState(int clientId)
        {
            var callsTimes = await _context.CallDataEntity
                .Where(call => call.ClientId == clientId)
                .Select(call => new ClientsAnalyticsDto(call.CallDate, call.CallSessionTime))
                .ToListAsync();

            if (!callsTimes.Any())
                return NotFound();

            return Ok(callsTimes);
        }
    }
}
