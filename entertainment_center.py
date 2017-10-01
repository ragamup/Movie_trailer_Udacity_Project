import media
import fresh_movie

#Creating instances for the movie trailers

toy_story = media.Movie("Toy Story","A story of a boy and his toy","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on the way to save an outer world","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

dunkirk = media.Movie("Dunkirk","Its about the war between germans and british","https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg","https://www.youtube.com/watch?v=_cmgiys2n1o")

lord = media.Movie("Lord Of The Rings","This movie is about the throne","https://upload.wikimedia.org/wikipedia/en/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif","https://www.youtube.com/watch?v=V75dMMIW2B4")

harry_potter = media.Movie("Harry Potter","This movie is about a wizard boy Harry","https://upload.wikimedia.org/wikipedia/commons/6/6e/Harry_Potter_wordmark.svg","https://www.youtube.com/watch?v=PbdM1db3JbY")

pursuit = media.Movie("Pursuit Of Happiness","This is a motivational movie","https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg","https://www.youtube.com/watch?v=89Kq8SDyvfg")


#Creating instances for the tv show trailers

got = media.Tv("Game Of Thrones","Its a Fight between the warriors for the throne","https://upload.wikimedia.org/wikipedia/en/9/93/AGameOfThrones.jpg","https://www.youtube.com/watch?v=1Mlhnt0jMlg")

dex = media.Tv("Dexter", "Its about a forensic technician specializing in blood spatter pattern analysis for the fictional Miami Metro Police Department","https://upload.wikimedia.org/wikipedia/en/c/c0/Dexter_TV_Series_Title_Card.jpg","https://www.youtube.com/watch?v=x9aGJeL_BRc")

friends = media.Tv("Friends", "Its a story between a group of friends","https://upload.wikimedia.org/wikipedia/commons/b/bc/Friends_logo.svg","https://www.youtube.com/watch?v=zGepgZYaWvM")

bbt = media.Tv("Big Bang Theory" , "The show is primarily centered on five characters","https://upload.wikimedia.org/wikipedia/en/7/7b/The_Big_Bang_Theory_%28Official_Title_Card%29.png","https://www.youtube.com/watch?v=WBb3fojgW0Q")

#creating a list for the movies and tv shows
movies = [ toy_story , avatar , dunkirk, lord , harry_potter, pursuit]

tvs= [got , dex , friends , bbt ]

#Calling a function to open a page for the list of movies and tv show trailers

fresh_movie.tv_movies_page(tvs)

fresh_movie.open_movies_page(movies)
