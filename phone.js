/** write a function to validate any global phone number using a regex
*/
define(function(){
    return function(phone){
        var regex = /^(\+?(\d{1,3}))?(\d{10})$/;
        return regex.test(phone);
    };
    }   
    