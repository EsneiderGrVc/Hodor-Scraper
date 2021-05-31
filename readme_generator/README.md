<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="Holberton School">
    <meta name="google" content="notranslate">

    <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">

    <title>Project: 0x07. Python - Test-driven development | Holberton Intranet</title>

    <link rel="stylesheet" media="all" href="/assets/application_blue-c2cf538a4ad8f1de97ef5d954e05e84e190e6472cc12e52af0267e535bfca79a.css" />
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="/assets/application-c73b57e94bf5c05a22f29487f5020ad02d30f68f8a9eb006b1282b6c73ebfcfc.js"></script>
    <link rel="shortcut icon" type="image/x-icon" href="/favicon_blue.ico" />
    <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="HGQNmdBYMg/QPnEpXpvxTySzOJWOO1zRm5Vf+Z3TJtoJtrTUDOkv2jLVqqIj4z7H0xZyz/JwmDA3uN2VDwlGeQ==" />

    <link rel="apple-touch-icon" href="/apple-touch-icon_blue.png">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Video player -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/ewwink/clappr-quality-selector-plugin@latest/quality-selector.js"></script>

    <!-- Store user timezone -->
    <script>
      Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
    </script>

    <!-- intro.js for interactive onboarding -->

    <!-- React -->
    <script src="/packs/js/application-82b58b009c8dd1b7404a.js"></script>
    <link rel="stylesheet" media="screen" href="/packs/css/application-3daba01b.css" />

  </head>

  <body class="
    signed_in
    env_production
    
    "
    translate="no"
    class="notranslate"
    data-theme-suffix="_blue"
    data-checker-special-theme="">

      <input type="hidden" id="hbtn-slack-url" value="https://holberton.enterprise.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
      <span class="name">Holberton</span>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i class="fa fa-info-circle"></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i class="fa fa-calendar"></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-current-projects-item" title="Projects"><a href="/dashboards/my_current_projects"><div class="icon "><i class="fa fa-code-fork"></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Professional track"><a href="/dashboards/my_professional_track"><div class="icon "><i class="fa fa-thumbs-o-up"></i></div><div class="visible-xs">Professional track</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews"><a href="/dashboards/corrections_i_can_make"><div class="icon "><i class="fa fa-check"></i></div><div class="visible-xs">QA Reviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i class="fa fa-commenting-o"></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i class="fa fa-question"></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i class="fa fa-graduation-cap"></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-concepts-item" title="Concepts"><a href="/dashboards/my_concepts"><div class="icon "><i class="fa fa-file-text"></i></div><div class="visible-xs">Concepts</div></a></li>
    
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i class="fa fa-comments"></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/dashboards/my_server"><div class="icon "><i class="fa fa-server"></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/dashboards/my_containers"><div class="icon "><i class="fa fa-terminal"></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/dashboards/my_peers"><div class="icon "><i class="fa fa-users"></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i class="fa fa-book"></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i class="fa fa-building"></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i class="fa fa-microphone"></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton.enterprise.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/002/930/thumb/me_and_my_bass.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210530%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210530T170243Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7cdf8fb65e9bc81d2c3b72db2ff377398f0f8689f54b46c604d6adc0d7182ef4')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i class="fa fa-info-circle"></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i class="fa fa-calendar"></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-current-projects-item" title="Projects"><a href="/dashboards/my_current_projects"><div class="icon "><i class="fa fa-code-fork"></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Professional track"><a href="/dashboards/my_professional_track"><div class="icon "><i class="fa fa-thumbs-o-up"></i></div><div class="visible-xs">Professional track</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews"><a href="/dashboards/corrections_i_can_make"><div class="icon "><i class="fa fa-check"></i></div><div class="visible-xs">QA Reviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i class="fa fa-commenting-o"></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i class="fa fa-question"></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i class="fa fa-graduation-cap"></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-concepts-item" title="Concepts"><a href="/dashboards/my_concepts"><div class="icon "><i class="fa fa-file-text"></i></div><div class="visible-xs">Concepts</div></a></li>
    
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i class="fa fa-comments"></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/dashboards/my_server"><div class="icon "><i class="fa fa-server"></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/dashboards/my_containers"><div class="icon "><i class="fa fa-terminal"></i></div><div class="visible-xs">Sandboxes</div></a></li>
    
    

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/dashboards/my_peers"><div class="icon "><i class="fa fa-users"></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i class="fa fa-book"></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i class="fa fa-building"></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i class="fa fa-microphone"></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton.enterprise.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/002/930/thumb/me_and_my_bass.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210530%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210530T170243Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7cdf8fb65e9bc81d2c3b72db2ff377398f0f8689f54b46c604d6adc0d7182ef4')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
      <div id="layout-bars">
        

        

        

        

          <a
    class="onair-container "
    data-target="#video_streams_current_modal"
    data-toggle="modal"
    href="#"
    title="Video Streaming in progress...">
    <div class="icon-container">
      <i class="fa fa-television" aria-hidden="true"></i>
      <i class="fa fa-podcast animate-flicker" aria-hidden="true"></i>
    </div>

    Watch the live stream
  </a>

      </div>

      <article class="">
        
<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x07. Python - Test-driven development</h1>


  <ul class="list-group metadata" id="project-metadata">
  <li class="list-group-item">
    <i class="fa fa-folder-open fa-fw"></i>
    Foundations - Higher-level programming ― Python
  </li>


    <li class="list-group-item">
      <i class="fa fa-user fa-fw"></i> By Guillaume, CTO at Holberton School
    </li>

    <li class="list-group-item">
      <i class="fa fa-cogs fa-fw"></i> Weight: 1
    </li>



      <li class="list-group-item">
        <i class="fa fa-calendar fa-fw"></i>
          Ongoing second chance project - started 05-24-2021, must end by 06-02-2021 (in 2 days)
          - you're done with <span id="student_task_done_percentage">0</span>% of tasks.
      </li>



      <li class="list-group-item">
        <i class="fa fa-check-square fa-fw"></i>
        QA review fully automated.
      </li>

      <div class="gap clean well">
  <h4>In a nutshell&hellip;</h4>
  <ul>


      <li>
        <strong>Auto QA review:</strong>
          121.0/167 mandatory
            &
            0.0/104 optional
      </li>
    <li>
      <strong>Altogether:</strong>
        &nbsp;<strong>72.46%</strong>
        <ul>
          <li>Mandatory: 72.46%</li>
          <li>Optional: 0.0%</li>
            <li>
              Calculation:&nbsp;
                  72.46% + (72.46% * 0.0%)
              &nbsp;==&nbsp;<strong>72.46%</strong>
            </li>
        </ul>
    </li>
  </ul>
</div>


</ul>



    <div id="project_id" style="display: none" data-project-id="246"></div>




      

      <div class="gap" id="project-description">
  <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif" alt="" style="" /></p>

<h2>Background Context</h2>

<h3>Important notice on intranet checks for Python projects</h3>

<p>Starting from today:</p>

<ul>
<li>Based on the requirements of each task, <strong>you should always write the documentation (module(s) + function(s)) and tests first</strong>, before you actually code anything</li>
<li>The intranet checks for Python projects won&rsquo;t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case. <strong>But not in the implementation of them!</strong></li>
<li><strong>Don&rsquo;t trust the user</strong>, always think about all possible edge cases</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/alaT1C9CeCbkRKh-yjMRww" title="doctest — Test interactive Python examples" target="_blank">doctest — Test interactive Python examples</a> (<em>until &ldquo;26.2.3.7. Warnings&rdquo; included</em>)</li>
<li><a href="/rltoken/cpEYbv_Z55QrSVRiuG5tUw" title="doctest – Testing through documentation" target="_blank">doctest – Testing through documentation</a> </li>
<li><a href="/rltoken/CELicn3K8hODQsWZak_h0g" title="Unit Tests in Python" target="_blank">Unit Tests in Python</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/a62WHzzKGDnndm6_qPJB1Q" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Python Test Cases</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>All your test files should be text files (extension: <code>.txt</code>)</li>
<li>All your tests should be executed by using this command: <code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case &ndash; The Checker is checking for tests!</li>
</ul>

</div>


      

        <h2 class="gap" id="project-quiz-questions-title">
    Quiz questions
  </h2>

  <div class="panel panel-default">
    <div class="panel-body">
        <p id="quiz_questions_collapse_toggle"></p>

      <section class="quiz_questions_show_container">
          <div class="quiz_question_item_container" data-role="quiz_question306" data-position="1">
            <div class=" clearfix" id="quiz_question-306">

    <h4 class="quiz_question">Question #0</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>/* Addition function */
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="306">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344951634" id="quiz-answer-1503344951634" data-quiz-question-id="306" data-quiz-answer-id="1503344951634" disabled="disabled" />
  <label for="quiz-answer-1503344951634">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344954613" id="quiz-answer-1503344954613" data-quiz-question-id="306" data-quiz-answer-id="1503344954613" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344954613">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question307" data-position="2">
            <div class=" clearfix" id="quiz_question-307">

    <h4 class="quiz_question">Question #1</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>&quot;&quot;&quot;&quot; Addition function &quot;&quot;&quot;
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="307">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344960922" id="quiz-answer-1503344960922" data-quiz-question-id="307" data-quiz-answer-id="1503344960922" disabled="disabled" />
  <label for="quiz-answer-1503344960922">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344963517" id="quiz-answer-1503344963517" data-quiz-question-id="307" data-quiz-answer-id="1503344963517" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344963517">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question308" data-position="3">
            <div class=" clearfix" id="quiz_question-308">

    <h4 class="quiz_question">Question #2</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>##########
# Addition function
##########
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="308">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344968631" id="quiz-answer-1503344968631" data-quiz-question-id="308" data-quiz-answer-id="1503344968631" disabled="disabled" />
  <label for="quiz-answer-1503344968631">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344972405" id="quiz-answer-1503344972405" data-quiz-question-id="308" data-quiz-answer-id="1503344972405" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344972405">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question309" data-position="4">
            <div class=" clearfix" id="quiz_question-309">

    <h4 class="quiz_question">Question #3</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>def add(a, b):
    &quot;&quot;&quot; Addition function &quot;&quot;&quot;
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="309">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344976219" id="quiz-answer-1503344976219" data-quiz-question-id="309" data-quiz-answer-id="1503344976219" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344976219">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344978977" id="quiz-answer-1503344978977" data-quiz-question-id="309" data-quiz-answer-id="1503344978977" disabled="disabled" />
  <label for="quiz-answer-1503344978977">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question310" data-position="5">
            <div class=" clearfix" id="quiz_question-310">

    <h4 class="quiz_question">Question #4</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this module correctly commented?</p>

<pre><code>#!/usr/bin/python3
&quot;&quot;&quot; 
    My calculation module
&quot;&quot;&quot;
import sys
...
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="310">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344983798" id="quiz-answer-1503344983798" data-quiz-question-id="310" data-quiz-answer-id="1503344983798" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344983798">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344986683" id="quiz-answer-1503344986683" data-quiz-question-id="310" data-quiz-answer-id="1503344986683" disabled="disabled" />
  <label for="quiz-answer-1503344986683">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question311" data-position="6">
            <div class=" clearfix" id="quiz_question-311">

    <h4 class="quiz_question">Question #5</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Is this module correctly commented?</p>

<pre><code>#!/usr/bin/python3
import sys

&quot;&quot;&quot; 
    My calculation module
&quot;&quot;&quot;
...
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="311">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503344991890" id="quiz-answer-1503344991890" data-quiz-question-id="311" data-quiz-answer-id="1503344991890" disabled="disabled" />
  <label for="quiz-answer-1503344991890">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503344994843" id="quiz-answer-1503344994843" data-quiz-question-id="311" data-quiz-answer-id="1503344994843" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503344994843">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->
        <div class="alert alert-info">
            <h4>Tips:</h4>
            <p>Docstring must be before import statements</p>

        </div>

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question312" data-position="7">
            <div class=" clearfix" id="quiz_question-312">

    <h4 class="quiz_question">Question #6</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Based on this code, what should all the test cases be? (select multiple)</p>

<pre><code>def uniq(list):
    &quot;&quot;&quot; Returns unique values of a list &quot;&quot;&quot;
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="312">
                <li class="">
  <input type="checkbox" name="quiz-answer-1503345028279" id="quiz-answer-1503345028279" data-quiz-question-id="312" data-quiz-answer-id="1503345028279" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345028279">
    <p>empty list</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345034707" id="quiz-answer-1503345034707" data-quiz-question-id="312" data-quiz-answer-id="1503345034707" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345034707">
    <p>list with one element (any type)</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345045706" id="quiz-answer-1503345045706" data-quiz-question-id="312" data-quiz-answer-id="1503345045706" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345045706">
    <p>list with 2 different element (same type)</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345056727" id="quiz-answer-1503345056727" data-quiz-question-id="312" data-quiz-answer-id="1503345056727" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345056727">
    <p>list with twice the same element (same type)</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345080984" id="quiz-answer-1503345080984" data-quiz-question-id="312" data-quiz-answer-id="1503345080984" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345080984">
    <p>list with more than 2 times the same element (same type)</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345098716" id="quiz-answer-1503345098716" data-quiz-question-id="312" data-quiz-answer-id="1503345098716" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345098716">
    <p>list with multiple types (integer, string, etc&hellip;)</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1503345131399" id="quiz-answer-1503345131399" data-quiz-question-id="312" data-quiz-answer-id="1503345131399" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1503345131399">
    <p>not a list argument (ex: passing a dictionary to the method)</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>


        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1167" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1167">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Integers addition
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1167" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__(&#39;0-add_integer&#39;).add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, &quot;School&quot;))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).__doc__)&#39; | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).add_integer.__doc__)&#39; | wc -l
3
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>0-add_integer.py, tests/0-add_integer.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1167">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1167" data-project-id="246" data-toggle="modal" data-target="#task-1167-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1167-users-done-modal" data-task-id="1167" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Integers addition"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1167" data-toggle="modal" data-target="#task-test-correction-1167-correction-modal" id="task-num-0-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1167-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. Integers addition"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1167">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1167">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1167">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1167" data-toggle="modal" data-target="#task-qa-review-1167-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1167-modal" data-correction-id="211503" data-task-id="1167">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">0. Integers addition</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1169" data-position="3" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1169">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Divide a matrix
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1169" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__(&#39;2-matrix_divided&#39;).matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>2-matrix_divided.py, tests/2-matrix_divided.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1169">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1169" data-project-id="246" data-toggle="modal" data-target="#task-1169-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1169-users-done-modal" data-task-id="1169" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Divide a matrix"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1169" data-toggle="modal" data-target="#task-test-correction-1169-correction-modal" id="task-num-1-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1169-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Divide a matrix"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1169">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1169">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1169">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1169" data-toggle="modal" data-target="#task-qa-review-1169-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1169-modal" data-correction-id="211503" data-task-id="1169">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">1. Divide a matrix</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1170" data-position="4" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1170">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Say my name
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1170" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__(&#39;3-say_my_name&#39;).say_my_name

say_my_name(&quot;John&quot;, &quot;Smith&quot;)
say_my_name(&quot;Walter&quot;, &quot;White&quot;)
say_my_name(&quot;Bob&quot;)
try:
    say_my_name(12, &quot;White&quot;)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>3-say_my_name.py, tests/3-say_my_name.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1170">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1170" data-project-id="246" data-toggle="modal" data-target="#task-1170-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1170-users-done-modal" data-task-id="1170" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Say my name"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1170" data-toggle="modal" data-target="#task-test-correction-1170-correction-modal" id="task-num-2-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1170-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Say my name"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1170">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1170">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1170">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1170" data-toggle="modal" data-target="#task-qa-review-1170-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1170-modal" data-correction-id="211503" data-task-id="1170">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">2. Say my name</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1171" data-position="5" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1171">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Print square
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1171" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__(&#39;4-print_square&#39;).print_square

print_square(4)
print(&quot;&quot;)
print_square(10)
print(&quot;&quot;)
print_square(0)
print(&quot;&quot;)
print_square(1)
print(&quot;&quot;)
try:
    print_square(-1)
except Exception as e:
    print(e)
print(&quot;&quot;)

guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be &gt;= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>4-print_square.py, tests/4-print_square.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1171">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1171" data-project-id="246" data-toggle="modal" data-target="#task-1171-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1171-users-done-modal" data-task-id="1171" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Print square"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1171" data-toggle="modal" data-target="#task-test-correction-1171-correction-modal" id="task-num-3-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1171-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Print square"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1171">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1171">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1171">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1171" data-toggle="modal" data-target="#task-qa-review-1171-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1171-modal" data-correction-id="211503" data-task-id="1171">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">3. Print square</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1172" data-position="6" id="task-num-4">
      <div class="panel panel-default task-card " id="task-1172">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Text indentation
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1172" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__(&#39;5-text_indentation&#39;).text_indentation

text_indentation(&quot;&quot;&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres&quot;&quot;&quot;)

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>5-text_indentation.py, tests/5-text_indentation.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1172">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1172" data-project-id="246" data-toggle="modal" data-target="#task-1172-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1172-users-done-modal" data-task-id="1172" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Text indentation"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1172" data-toggle="modal" data-target="#task-test-correction-1172-correction-modal" id="task-num-4-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1172-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "4. Text indentation"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1172">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1172">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1172">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1172" data-toggle="modal" data-target="#task-qa-review-1172-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1172-modal" data-correction-id="211503" data-task-id="1172">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">4. Text indentation</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1857" data-position="7" id="task-num-5">
      <div class="panel panel-default task-card " id="task-1857">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Max integer - Unittest
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1857" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/qMqF1bBJXSAIjg8tugitHQ" title="unittest module" target="_blank">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
&quot;&quot;&quot;Module to find the max integer in a list
&quot;&quot;&quot;


def max_integer(list=[]):
    &quot;&quot;&quot;Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    &quot;&quot;&quot;
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
&quot;&quot;&quot;Unittest for max_integer([..])
&quot;&quot;&quot;
import unittest
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>tests/6-max_integer_test.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1857">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1857" data-project-id="246" data-toggle="modal" data-target="#task-1857-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1857-users-done-modal" data-task-id="1857" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Max integer - Unittest"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1857" data-toggle="modal" data-target="#task-test-correction-1857-correction-modal" id="task-num-5-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1857-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "5. Max integer - Unittest"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1857">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1857">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1857">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1857" data-toggle="modal" data-target="#task-qa-review-1857-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1857-modal" data-correction-id="211503" data-task-id="1857">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">5. Max integer - Unittest</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1173" data-position="100" id="task-num-6">
      <div class="panel panel-default task-card " id="task-1173">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Matrix multiplication
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1173" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that multiplies 2 matrices:</p>

<ul>
<li><p>Read: <a href="/rltoken/gG3TcWESGFqiZzHNlMbEKA" title="Matrix multiplication - only Matrix product (two matrices)" target="_blank">Matrix multiplication - only Matrix product (two matrices)</a></p></li>
<li><p>Prototype: <code>def matrix_mul(m_a, m_b):</code></p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be validated with these requirements in this order</p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be an list of lists of integers or floats:</p>

<ul>
<li>if <code>m_a</code> or <code>m_b</code> is not a list: raise a <code>TypeError</code> exception with the message <code>m_a must be a list</code> or <code>m_b must be a list</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a list of lists: raise a <code>TypeError</code> exception with the message <code>m_a must be a list of lists</code> or <code>m_b must be a list of lists</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is empty (it means: <code>= []</code> or <code>= [[]]</code>): raise a <code>ValueError</code> exception with the message <code>m_a can&#39;t be empty</code> or <code>m_b can&#39;t be empty</code></li>
<li>if one element of those list of lists is not an integer or a float: raise a <code>TypeError</code> exception with the message <code>m_a should contain only integers or floats</code> or <code>m_b should contain only integers or floats</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a rectangle (all &lsquo;rows&rsquo; should be of the same size): raise a <code>TypeError</code> exception with the message <code>each row of m_a must be of the same size</code> or <code>each row of m_b must be of the same size</code></li>
</ul></li>
<li><p>If <code>m_a</code> and <code>m_b</code> can&rsquo;t be multiplied: raise a <code>ValueError</code> exception with the message <code>m_a and m_b can&#39;t be multiplied</code></p></li>
<li><p>You are not allowed to import any module</p></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__(&#39;100-matrix_mul&#39;).matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>100-matrix_mul.py, tests/100-matrix_mul.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1173">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1173" data-project-id="246" data-toggle="modal" data-target="#task-1173-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1173-users-done-modal" data-task-id="1173" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Matrix multiplication"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1173" data-toggle="modal" data-target="#task-test-correction-1173-correction-modal" id="task-num-6-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1173-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "6. Matrix multiplication"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1173">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1173">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1173">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1173" data-toggle="modal" data-target="#task-qa-review-1173-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1173-modal" data-correction-id="211503" data-task-id="1173">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">6. Matrix multiplication</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1174" data-position="101" id="task-num-7">
      <div class="panel panel-default task-card " id="task-1174">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Lazy matrix multiplication
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1174" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a function that multiplies 2 matrices by using the module <a href="/rltoken/3_FcFGqtWsHzii5VrujTWA" title="NumPy" target="_blank">NumPy</a></p>

<p>To install it: <code>pip3 install numpy==1.15.0</code></p>

<ul>
<li>Prototype: <code>def lazy_matrix_mul(m_a, m_b):</code></li>
<li>Test cases should be the same as <code>100-matrix_mul</code> but with new exception type/message</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__(&#39;101-lazy_matrix_mul&#39;).lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1174">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1174" data-project-id="246" data-toggle="modal" data-target="#task-1174-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1174-users-done-modal" data-task-id="1174" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "7. Lazy matrix multiplication"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1174" data-toggle="modal" data-target="#task-test-correction-1174-correction-modal" id="task-num-7-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1174-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "7. Lazy matrix multiplication"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1174">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1174">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1174">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1174" data-toggle="modal" data-target="#task-qa-review-1174-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1174-modal" data-correction-id="211503" data-task-id="1174">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">7. Lazy matrix multiplication</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1166" data-position="102" id="task-num-8">
      <div class="panel panel-default task-card " id="task-1166">
  <span id="user_id" data-id="2930"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. CPython #3: Python Strings
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2930"></span>

    

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1166" data-correction-id="211503">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/2c4f2b92514745519f833afdf5bc5f3eaff8c6ca.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210530%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210530T170243Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=31849acf0f26096329c1bb0f679d0978c788b53a3767a43c91a9fe933e8d5e67" alt="" style="" />
<br /></p>

<p>Create a function that prints Python strings.</p>

<ul>
<li>Prototype: <code>void print_python_string(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid string, print an error message (see example)</li>
<li>Read: <a href="/rltoken/IOH653eTNMgJcUTeV2jM2w" title="Unicode HOWTO" target="_blank">Unicode HOWTO</a></li>
</ul>

<p>About:</p>

<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL(&#39;./libPython.so&#39;)
lib.print_python_string.argtypes = [ctypes.py_object]
s = &quot;The spoon does not exist&quot;
lib.print_python_string(s)
s = &quot;ложка не существует&quot;
lib.print_python_string(s)
s = &quot;La cuillère n&#39;existe pas&quot;
lib.print_python_string(s)
s = &quot;勺子不存在&quot;
lib.print_python_string(s)
s = &quot;숟가락은 존재하지 않는다.&quot;
lib.print_python_string(s)
s = &quot;スプーンは存在しない&quot;
lib.print_python_string(s)
s = b&quot;The spoon does not exist&quot;
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n&#39;existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>102-python.c</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1166">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1166" data-project-id="246" data-toggle="modal" data-target="#task-1166-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1166-users-done-modal" data-task-id="1166" data-project-id="246">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "8. CPython #3: Python Strings"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default" data-task-id="1166" data-toggle="modal" data-target="#task-test-correction-1166-correction-modal" id="task-num-8-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1166-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "8. CPython #3: Python Strings"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1166">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1166">
        <i class="fa fa-info-circle" aria-hidden="true"></i>
    </button>
    <div class="help-container" data-task-id="1166">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i class="fa fa-check-circle" aria-hidden="true"></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                Text answer fail
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>




      <button class="btn btn-default" data-task-id="1166" data-toggle="modal" data-target="#task-qa-review-1166-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1166-modal" data-correction-id="211503" data-task-id="1166">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">8. CPython #3: Python Strings</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>








  </div>
</div>

      </article>

      <div class="copyright">Copyright &copy; 2021 Holberton School. All rights reserved.</div>
    </main>

      <button class="btn btn-primary" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
    <i class="fa fa-search" aria-hidden="true"></i>
    <i class="fa fa-window-minimize" aria-hidden="true"></i>
</button>

      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>

        <div class="modal fade" id="video_streams_current_modal">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Video streaming</h4>
            </div>
            <div class="modal-body">
                <ul class="streams list-group"></ul>
                <div class="player">
                    <div class="header">
                        <div class="back"><i class="fa fa-chevron-left" aria-hidden="true"></i></div>
                        <div class="title"></div>
                    </div>
                    <div id="video_streams_current_modal_player"></div>
                </div>
                <div class="spinner">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="error"></div>
            </div>
        </div>
    </div>
</div>



      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '2930'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>



      <input id="checker_pride_assets" type="hidden" value="[]">

      
  </body>
</html>