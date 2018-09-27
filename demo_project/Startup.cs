using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using UserService;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using UserService.Models;
using Microsoft.EntityFrameworkCore;

namespace container_solution
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            // Console.WriteLine("AAAAAA " + Configuration.GetConnectionString("ServiceContext"));
            // string connectionString = Configuration.GetConnectionString("ServiceContext");
            string db_server = Environment.GetEnvironmentVariable("DB_SERVER");
            string db_port = Environment.GetEnvironmentVariable("DB_PORT");
            string db_username = Environment.GetEnvironmentVariable("DB_USERNAME");
            string db_password = Environment.GetEnvironmentVariable("DB_PASSWORD");
            string db_database = Environment.GetEnvironmentVariable("DB_DATABASE");

            string connectionString = 
                $@"
                Persist Security Info=true;
                Server={db_server};
                Port={db_port};
                Username={db_username};
                Password={db_password};
                Database={db_database};
                Integrated Security=false;
                "; 

            services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_1);
            services.AddEntityFrameworkNpgsql().AddDbContext<ServiceContext>(
                opt => opt.UseNpgsql(connectionString)
            );
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseMvc();
        }
    }
}
