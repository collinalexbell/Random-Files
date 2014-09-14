/**
* Created with Rouge.
* User: SlightlyCyborg
* Date: 2014-09-09
* Time: 03:46 PM
* To change this template use Tools | Templates.
*/
fs = require('fs')
module.exports.get_contacts = function(callback){
    
    fs.readFile('./contacts.csv', 'utf8', function (err,data) {
      if (err) {
        return console.log(err);
      } 
        var csv = require('csv');


        csv.parse(data, {comment: '#'}, function(err, output){

            objectify(output, callback)
        });
    });

    var objectify = function(output, callback){
        var descriptors = output[0]
        var contacts = []
        for (i in output){
            if (i >0){
                var new_obj = {}
                for (j in descriptors){
                    new_obj[descriptors[j]] = output[i][j]
                }
                contacts.push(new_obj)
            }
        }
        callback(contacts);
        

    }
}