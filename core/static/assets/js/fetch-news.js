window.addEventListener("load", function() {
    load_tweets();
});

function load_tweets() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.response);
            var i = 0;
            let tweets = document.getElementById("tweets");
            let closed=true;
            let content = "";
            tweets.innerHTML='<button onclick="renderEmbeds()" class="btn btn-xs btn-default">Render Embedded Tweets</button>';
            for(tweet of data){
                if(i%3==0){
                    content+='<div class="row mb-5">';
                    closed=false;
                }
                content+='<div class="col-md-4">';
                content+=tweet['oembed'];
                content+='</div>';
                if(i%3==2){
                    content+='</div>'
                    tweets.innerHTML+=content;
                    closed = true;
                    content = "";
                }
                i++;
            }
            if(!closed){
                content+='</div>';
                tweets.innerHTML+=content;
            }
        }
    };

    xhttp.open("GET", "tweets");
    xhttp.send();
}
