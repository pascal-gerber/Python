print("1. Basics\n2. Texts\n3. Text allinement\n4. Images and gifs\n"+
      "5. Moving texts \"Item\"\n6. text styles HTML\n7. Guide of HTML"+
      "\n8. CSS Stylesheet text customisations\n9. ")
a = input("write a number:")

if(a=="1"):
    print("\n<!DOCTYPE html>\n<html>\n<head>\n<title>"+
        "\n\n</title>\n</head>\n<body>\n\n"+
        "</body>\n</html>\n")
elif(a=="2"):
    print("\n<p>this is a paragraph</p>\n<h1>This is a title</h1>"+
        "\n<h2>this is a subtitle</h2>\n<h4>h3 also exists but its bigger than this tiny text</h4>")
elif(a=="3"):
    print("\n<p>first line<br>second line</p>\n\n<pre>\nthis\nwill\nbe\nwritten\nlike\nthat"+
        "\n</pre>\n\n<ul>\n   <li>apples</li>\n   <li>Bread</li>\n</ul>")

elif(a=="4"):
    print("\n<img src=\"selectedpicture.jpg\" alt=\"Title of the picture\">\nAdding size to the picture is written this way"+
          "\nwidth=\"500\" height=\"600\"\n\nfor a Gif you write this"+
          "\n<img src=\"Gif file.gif\" alt=\"Gif\">"+
          "\n\n for a Background picture, put that in the head section"+
          "\n<div style=\"background-image: url(\'background.jpg\');>")

elif(a=="5"):
    print("\n<marquee direction=\"Left, right, up or down\">Moving text and images</marquee>")

elif(a=="6"):
    print("\nFor any fonts \"example: Arial\" from Word:\n\n<font face=\"Arial\">this text is arial</font>\n\n"+
          "For slidding text use marquee:\n\n<marquee direction=\"down\">This text slides down.</marquee>")
elif(a=="7"):
    print("\nA website starts off using 1 Folder(root) that contains other folders(parents).\nEach of these folders contain other Folder or"+
          "HTML + CSS Files (child).\n\n<link rel=\"stylesheet\" type=\"text/css\" href=\"stylesheet.css\" media=\"screen\"/>")
elif(a=="8"):
    print("\np.custom {\n  background-color: red;\n}"+"\nor\n.main-font {font-family: Class, \"Calibri\", Times, serif;}"+
          "\nnotice : serif is OPTIONNAL)")

    
input()








