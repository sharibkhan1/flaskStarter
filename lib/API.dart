import 'package:http/http.dart' as http; // Import the http package

Future<String> Getdata(String url) async {
  // Convert the string URL to a Uri object
  Uri uri = Uri.parse(url);

  // Use the Uri object when making the request
  http.Response response = await http.get(uri);
  return response.body;
}
