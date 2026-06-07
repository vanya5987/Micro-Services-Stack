using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace call_data_microcervice.Migrations
{
    /// <inheritdoc />
    public partial class Addedcalldatetime : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<DateTime>(
                name: "CallDate",
                table: "CallDataEntity",
                type: "timestamp with time zone",
                nullable: false,
                defaultValue: new DateTime(1, 1, 1, 0, 0, 0, 0, DateTimeKind.Unspecified));
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "CallDate",
                table: "CallDataEntity");
        }
    }
}
