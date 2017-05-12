/**
 MIT License

 Copyright (c) 2016 Michael Lant, Bogdan Pshonyak, Yegor Shemereko

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
 */

/**
 * This is all the javasript needed for Newsletter sign-up page to operate
 */

/**
 * The function that handles the submit from the newsletter form
 */
$("#newsletter-form").on("submit", function (e) {

    e.preventDefault();

    var $email = $("#email").val();
    var $errorText = $("#email-error");

    console.log($email);

    $.ajax({
        url: '/api/newsletter.php',
        type: 'POST',
        data: {
            email: $email,
        },
        success: function(result) {

            //handle errors
            if (result.status === 403) {
                $errorText.text("Error: " + result.msg);
                $errorText.removeClass("hide");
            } else {
                $errorText.addClass("hide");
                $("#alert-success").removeClass("hide");
            }

        }
    });

});
