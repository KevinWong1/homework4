<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.css" rel="stylesheet" />
  <link rel="stylesheet" href="../docs/css/styles.css" />
  <link href="https://fonts.googleapis.com/css?family=Baloo+Da+2|Fredoka+One&display=swap" rel="stylesheet" />
  <title>{{ title }}</title>
</head>

<body>
  <div class="container">
    <div class="row">
      <div class="rounded-lg strikingbackground col min_height">
        <h1 class="text-center">Kevin Wong</h1>
        <img src="../docs/img/pic1.jpg" class="img-fluid img-thumbnail catleft" />

        {% for page in pages %}
        <a href="{{ page.title }}.html">
          <p>
            <button type="button" class="btn buttoncss 
            
            {% if page.title ==  title  %}
            active
            {% else %}
            pass
            {% endif %}

            ">
              {{ page.title }} <i class="fas fa-cat"></i>
            </button>
          </p>
        </a>
        {% endfor %}

      </div>
      <!-- end of left side panel -->
      <!-- replace content with contents of each individual page using python script-->
      {{ content }}
      <!-- start of bottom -->
    </div>
  </div>
</body>

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
  integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
  integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
  integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<p class="buttoncss">� 2020-{{ year }}</p>

</html>