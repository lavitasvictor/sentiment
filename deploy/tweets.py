<!DOCTYPE html>

<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>tweets.py : /home/vbrn/deploy/tweets.py : Editor : vbrn : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="tweets.py : /home/vbrn/deploy/tweets.py : Editor : vbrn : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="/static/CACHE/css/afa5e20fceeb.css" type="text/css" media="screen" />
        <link rel="stylesheet" href="/static/CACHE/css/ad9d1f2ab435.css" type="text/css" media="screen" />

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "1UJQrD2blzJtnAgsVHIGu3Rv0W69guRk";
        </script>
        <script type="text/javascript" src="/static/CACHE/js/4c6fed4396b4.js"></script>
        

        <script type="text/javascript" src="/static/CACHE/js/b13f6a2104a0.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          save: "/user/vbrn/files/home/vbrn/deploy/tweets.py",
          check_hash: "/user/vbrn/files/home/vbrn/deploy/tweets.py",
          run: "/user/vbrn/files/home/vbrn/deploy/tweets.py" + "?run",
          update_editor_mode_preference: "/user/vbrn/account/update_editor_mode_preference",
        });
        var filename = "/home/vbrn/deploy/tweets.py";
        var hash = "e6e8c418cb0f0328aed303083e80adf6";
        var interpreter = "python3.5";

        
            Anywhere.Editor.InitialiseAce(ace, Anywhere.urls, filename, hash, interpreter);
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/vbrn/files/sharing/",
            csrfToken: "1UJQrD2blzJtnAgsVHIGu3Rv0W69guRk",
            path: "/home/vbrn/deploy/tweets.py"
          }
        );

      });
    </script>

        

        <!-- Le fav and touch icons -->
        <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">



    </head>

     <body>
        
    <nav class="navbar" role="banner">
        <div id="id_internal_nav_bar_container" class="container fluid">

            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".right_hand_links" aria-expanded="false">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/"><img id="id_logo" src="/static/anywhere/images/logo-234x35.png" height="35" title="PythonAnywhere logo" alt="PythonAnywhere logo" /></a>
            </div>

            <div class="collapse navbar-collapse right_hand_links">
                <div class="row">
                    <ul id="id_header_links" class="nav navbar-nav navbar-right ">
                        <li><a id="id_feedback_link" class='feedback_link' href="">Send feedback</a></li>
                        <li><a id="id_forums_link" href="/forums/">Forums</a></li>
                        <li><a href="https://help.pythonanywhere.com/" id="id_help_link">Help</a></li>
                        <li><a href="https://blog.pythonanywhere.com/" id="id_blog_link">Blog</a></li>
                        
                        
                            <li><a href="/user/vbrn/" id="id_dashboard_nav_link">Dashboard</a></li>
                            <li><a href="/user/vbrn/account/" id="id_account_link">Account</a></li>
                            <li>
                            <form class="navbar-form" action="/logout/" method="POST">
                              <input type='hidden' name='csrfmiddlewaretoken' value='1UJQrD2blzJtnAgsVHIGu3Rv0W69guRk' />
                              <button type="submit" class="btn btn-link" id="id_logout_link">Log out</button>
                            </form>
                            </li>
                        
                    </ul>
                </div>

                
                    <div class="row nice_dropdown header_second_row">

                        

                        

                        
                        

                        

                        

                    </div>
                
            </div>
        </div>
    </nav>

    



        
    


        

<div>

    <div id="id_editor_toolbar">

      <div id="id_editor_messages">
        

      </div>

      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/vbrn/files/">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/vbrn/files/home">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/vbrn/files/home/vbrn">vbrn</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/vbrn/files/home/vbrn/deploy">deploy</a><span class="breadcrumb_entry">/</span><span class="breadcrumb_entry breadcrumb_terminal">tweets.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
      <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
      <div id="id_editor_buttons_right" class="form-inline">
          <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
          
              <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
              <select id="id_keybinding_mode_select" class="form-control input-sm">
                  <option value="normal">Normal</option>
                  <option value="vim">Vim</option>
              </select>
          
          <button id="id_display_sharing_options" class="btn btn-sm btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
            <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
            Share
          </button>
          
            <button id="id_save" class="btn btn-sm btn-success" title="Save (Ctrl + S)">
              <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
              Save
            </button>
            <button id="id_save_as" class="btn btn-sm btn-default" title="Save As">Save as...</button>
          
          
          <button class="btn btn-sm btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
          

          
          
            <form class="reload_web_app" style="display: inline" method="POST" action="/user/vbrn/webapps/vbrn.pythonanywhere.com/reload">
                <button class="btn btn-sm btn-default" type="submit" title="Reload vbrn.pythonanywhere.com">
                    <i class="glyphicon glyphicon-refresh"></i>
                </button>
                <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
                <div style="display: none; clear: both;" class="error_message generic_error">
                    There was a problem. If this keeps happening, please <a href="" class="feedback_link">send us feedback</a>.
                </div>
                <div style="display: none; clear: both;" class="error_message slow_startup_error">
                    Your webapp took a long time to reload. It probably reloaded, but we were unable to check it.
                </div>
                <div style="display: none; clear: both;" class="error_message virtualenv_error">
                    There is a problem with your virtualenv setup. Look at the <b>virtualenv</b> section on the web app tab for details.
                </div>
                <div style="display: none; clear: both;" class="error_message cname_error">
                    There is a problem with your DNS configuration. Take a look at the <b>DNS setup</b> section on the web app tab for details.
                </div>
            </form>
          
          


        </div>
        <div class="clear"></div>
    </div>

    <div id="id_ide_split_panes">

        
            <div id="id_editor">#!/usr/bin/env python3

# TODO
import sys, os
from termcolor import colored

def main():
    #accepts one and only one command-line argument, the screen name for a user on Twitter,
    if len(sys.argv) != 2:
        sys.exit(&quot;Usage: ./tweets word&quot;)

    #queries Twitter’s API for a user’s most recent 50 tweets,
    #helpers.py get_user_timeline
    os.environ.update(API_KEY=&#39;l1pY3oefdEilyJati2HArX5Eg&#39;)
    os.environ.update(API_SECRET=&#39;Jkgu5VifjboJ2QFZePuQR5sNWEmT9Qjh7hYWyfv26kSFsmI61P&#39;)
    import helpers
    #check if successful error if unsuccessful sys.exit
    try:
        tweets=helpers.get_user_timeline(sys.argv[1][1:],count=50)
    except:
        sys.exit(&quot;There was some problem&quot;)
    
    if not tweets:
        sys.exit(&quot;There was some problem&quot;)
    
    #analyzes the sentiment of each of those tweets, and
    #tokenize tweet
    #use tweet tokenizer to split a tweet into list of words(shorter strings)
    
    #analyse tweet to check if it is positive or negatives
    

    #outputs each tweet’s score and text, colored in green if positive, red if negative, and yellow otherwise.
    # absolute paths to lists
    positives = os.path.join(sys.path[0], &quot;positive-words.txt&quot;)
    negatives = os.path.join(sys.path[0], &quot;negative-words.txt&quot;)

    # instantiate analyzer
    from analyzer import Analyzer
    analyzer = Analyzer(positives, negatives)
    for tweet in tweets:
        score=analyzer.analyze(tweet)
        if score &gt; 0.0:
            print(colored(tweet, &quot;green&quot;))
        elif score &lt; 0.0:
            print(colored(tweet, &quot;red&quot;))
        else:
            print(colored(tweet, &quot;yellow&quot;))


    
if __name__ == &quot;__main__&quot;:
    main()
</div>
        

        <div id="id_ide_console">
            
                <div id="id_ide_console_pane_buttons">
                    <center>
                        
                            <button class="btn btn-large btn-info run_button" title="Save &amp; Run (Ctrl + R)">&gt;&gt;&gt; Run this file</button>
                            <button class="btn btn-large btn-info bash_console_here" title="Start a Bash console in this folder">$ Bash console here</button>
                        
                    </center>
                </div>
                <iframe style="display: none" id="id_console" name="console" class="soft_keyboard_sensitive">
                </iframe>
                <div style="display: none;" class="console_limit_reached">
                    <div class="container">
    <div class="row">
        <div class="col-md-5 col-md-offset-3 well">
            <h1>Console limit reached :-/</h1>

            <p>
            With your current PythonAnywhere account you can have up to
            2 consoles.  You can
            have more if you
            <a href="/user/vbrn/account/">upgrade your account</a>!

            <p>
            Alternatively, if you don't feel like paying us more money, you
            can <a href="/user/vbrn/consoles/">kill some consoles on your Consoles page</a>.
        </div>
    </div>
</div>


                </div>
            
        </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
        <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
        <div class="dialog_buttons">
            <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
            <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
        </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
        <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
        <div class="dialog_buttons">
            <button id="id_force_save" class="btn btn-danger">Force Save</button>
            <button id="id_cancel_save" class="btn btn-default">Cancel</button>
        </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
        <form class="form-inline">
            <div class="form-group">
                <label for="id_save_as_path">Please enter a path:</label>
                <input id="id_save_as_path" class="form-control" style="width: 100%;" />
            </div>
            <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
            <p>
                <span id="id_save_as_error" class="error_message"></span>
            </p>
            <div class="dialog_buttons">
                <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
                <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
            </div>
        </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

</div>


        

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" class="pa_hidden">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
