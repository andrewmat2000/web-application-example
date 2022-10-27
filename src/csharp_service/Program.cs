using Asd.HttpLib.AspNet;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddAsdHttpServer();

var app = builder.Build();
app.UseAsdHttpService<CsharpService.HttpServer>();

app.Run();
