import 'package:http/http.dart' as http;

fetchdata(String url) async {
  try {
    http.Response response = await http.get(Uri.parse(url)).timeout(Duration(seconds: 10));
    return response.body;
  } catch (e) {
    print('Error fetching data: $e');
    return null;
  }
}
