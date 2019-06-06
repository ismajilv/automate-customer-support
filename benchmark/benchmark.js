var apiBenchmark = require('api-benchmark');
var fs = require('fs');

var service = {
  server1: 'http://localhost/'
};



var routes = {
		method: '123'};

apiBenchmark.measure(service, routes, function(err, results){
  apiBenchmark.getHtml(results, function(error, html){
    fs.writeFileSync('benchmarks.html', html);
  });
});
