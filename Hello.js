/**
* Created with Rouge.
* User: SlightlyCyborg
* Date: 2014-09-09
* Time: 01:35 PM
* To change this template use Tools | Templates.
*/
var express = require('express');
var app = express();

app.get('/', function(req, res){
  res.send('Live Edit');
});

app.listen(3000);


var contact_parser = require("contact_parser")
var mission_statement ={text:"Tell me UTOP's mission statement", funct:function(callback){
    	var statement = "The UTOP mission is to provide the university community with outdoor adventure, recreation and education. Programs will be inclusive to people of all backgrounds and abilities and will contribute to the holistic well-being and academic experience of the university."
    	console.log(statement)
        callback();
	}
}

var make_tea = {
    text:"Make tea",
    funct:function(callback){
    	console.log("Sadly, tea will have to be made by you for the moment")
        callback();
    }
}

var contact_list = {
    text:"Show Contact List",
    funct:function(callback){
    	contact_parser.get_contacts(callback)
    }
}

//Main Loop
var main_loop = function(){
    console.log("Welcome to the UTOP command center. How can I help you?")
    choices = [mission_statement, make_tea, contact_list]

    num = 0
    for (var i in choices){
      console.log(num + ") " + choices[i].text)  
      num ++
    }

    var readline = require('readline');

    var rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });


    rl.question("What is our next adventure? (please enter a number) ", function(answer) {
      // TODO: Log the answer in a database
      select(answer)

      rl.close();
    });
}

var select = function(choice_num){
  if(choices[choice_num] != undefined){
      console.log("Your Choice is: " + choices[choice_num].text)
      choices[choice_num].funct(main_loop)
  }
  else{
      console.log("Invalid Choice")
  }
}

main_loop();



