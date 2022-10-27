using HttpMethod = Asd.HttpLib.HttpMethod;

namespace CsharpService;

public class HttpServer {
  [HttpMethod("get_secret")]
  public string GetSecret() {
    return "c#";
  }
}