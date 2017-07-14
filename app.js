var express = require("express"),  
    app = express(),
    bodyParser  = require("body-parser"),
    methodOverride = require("method-override");
    mongoose = require('mongoose');

app.use(bodyParser.urlencoded({ extended: false }));  
app.use(bodyParser.json());  
app.use(methodOverride());

var router = express.Router();
////////////////////////////////////////////////////// PUNTO 1
//localhost:3333      <--- como usarlo
router.get('/', function(req, res) {  
   res.send("Bienvenidos a la Prueba técnica de Huteck!");
});


////////////////////////////////////////////////////// PUNTO 3

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.post('/', function(req, res) {
	var req = 'https://jsonplaceholder.typicode.com/posts'
    var body1 = req.body.body

    res.send("Consumiendo:"+ ' ' + body1);
});

//////////////////////////////////////////////////////

////////////////////////////////////////////////////// PUNTO 2 GET
//localhost:3333/api    <--- como usarlo
router.get('/api', function(req, res) {  
   res.send("hola!");
});
//////////////////////////////////////////////////////

////////////////////////////////////////////////////// PUNTO 2 POST
//localhost:3333/api/user?nom=carlos     <--- como usarlo
app.get('/api/user', function(req, res) {
  //var user_id = req.param('id');
  //var token = req.param('token');
  var nom = req.param('nom');  

  //res.send(user_id + ' ' + token + ' ' + nom);
  res.send("Hola"+ ' ' + nom);
});


app.use(router);

app.listen(3333, function() {  
  console.log("Node server running on http://localhost:3333");
});