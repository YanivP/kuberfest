using Microsoft.EntityFrameworkCore;

namespace UserService.Models
{
    public class UserModel
    {
        public long Id {get; set;}
        public string Name {get; set;}
    }

    public class ServiceContext : DbContext
    {
        // When used with ASP.net core, add these lines to Startup.cs
        //   var connectionString = Configuration.GetConnectionString("BlogContext");
        //   services.AddEntityFrameworkNpgsql().AddDbContext<BlogContext>(options => options.UseNpgsql(connectionString));
        // and add this to appSettings.json
        // "ConnectionStrings": { "BlogContext": "Server=localhost;Database=blog" }

        public ServiceContext(DbContextOptions<ServiceContext> options) : base(options) { }
        public DbSet<UserModel> Users { get; set; }
    }
}