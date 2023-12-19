using BlogApp.Application;
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");
var uiInstance = new UI();
app.Run();
