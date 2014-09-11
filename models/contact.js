/**
* Created with Rouge.
* User: SlightlyCyborg
* Date: 2014-09-10
* Time: 02:46 PM
* To change this template use Tools | Templates.
*/
var parser = require('contact_parser.js')
var async = require('async')
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');
var model = mongoose.model('contact', { name: String, email: String, phone: String });


var Contact = function(contact_obj){
    var that = this
    this.name = contact_obj.name
    this.phone = contact_obj.phone
    this.email = contact_obj.email
    this.model = model;
    this.save = function(done){
        var new_contact = new that.model({name:that.name, email:that.email, phone:that.phone})
        new_contact.save(function(err){
            if(err) throw err
            if (done) done()
        })

    }
    
}







module.exports = Contact
module.exports.clear =  function(done){
     model.remove(function(err){
         if (err) throw err
         done()
     });
}
module.exports.find = function(obj, func){
	model.findOne(obj, func)
}

module.exports.import = function(file_name, callback){
    parser.get_contacts(function(contacts){
       	var saves = []
        for (i in contacts){
           var new_contact = new Contact(contacts[i])
           saves.push(new_contact.save)
           
        }
        async.parallel(saves, callback)
        
        
    })
    
}