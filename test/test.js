var assert = require("assert")
var Contact = require("models/contact.js")


describe('Contact', function(){
    describe('#save()',function(){
        it('should save without error', function(done){
            var contact = new Contact({name:'Collin Bell', phone:'8656034782'});
            contact.save(done)
        })
    })
    describe('#clear()', function(){
    	it('should clear ALL contacts from db', function(done){
             Contact.clear(done)
        })
    })
    describe('#get_contact()', function(){
        it('should get contact information from name', function(done){
            var contact = new Contact({name:'Collin Bell', email:'collinandtheearth@gmail.com', phone:'8656034782'});
            contact.save(function(){
                Contact.find('Collin Bell', function(err, cont){
                	console.log(cont)
                    assert.equal(cont.phone,'8656034782')
                	done()
                  
                })
                
            })
            
        })
        
    })
    
    describe('#import_contact()', function(){
        it('should import contacts from CSV', function(done){
            Contact.clear(function(){
            	Contact.import('contacts.csv', function(){
                    Contact.find({name:new RegExp('^Kyle')}, function(err, cont){
                        assert.equal(cont.name, 'Kyle Hodges')
                        Contact.find({name:'Georgie Kerber'}, function(err, cont1){
                            assert.equal(cont1.name, 'Georgie Kerber')
                            done()
                        })
                    })
                })   
            })
        })
    })


})