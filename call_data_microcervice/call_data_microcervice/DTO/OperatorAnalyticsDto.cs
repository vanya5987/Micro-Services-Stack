namespace call_data_microcervice.DTO
{
    public record OperatorAnalyticsDto
    (
        int CallsCount,
        float CallsAverage,
        float CallsSum
    );
}
