## Quick start
1. `git clone `
1. `docker-compose build`
1. Create this env file:
```
DATABASE_URL=postgres://postgres@db:5432/postgres
SECRET_KEY=putyourfavoritesonglyrichere
DEBUG=True
```
1. `docker-compose up`
1. Open another terminal window.
1. `docker-compose run nginx ./hoot/manage.py loaddata get_fixture.json `
 
1. `cd frontend`
1. `npm install`
1. `npm start`
1. go to `localhost:3000` in web browser


## notes for neil
1. Fix data from spreadsheets function   ✓
2. Add recommended search ✓
3. fix url encoding/decoding bugs ✓?
3. Keyboard shortcuts (focus search, clear search) ✓
4. nginx deployment strategy ✓
1. Embedding pdfs and colors ✓
1. Make section home show all entries for section ✓
1. Make homepage show all entries ✓
1. Why is "10 Questions" not working (turns out django doesn't like escaped ampersands)
1. ~There were duplicates in the spread sheet feels bad man~ nope there were not
1. Don't send request for recommended results when on section homepage ✓
1. Don't send request for sections, quick links and such every time we search.
1. Fix everything in views to use "sections" not section ✓
1. Logging
1. logging stats ✓
1. Multiple sources of truth in Header (query) and Sidebar (section)
1. Honestly just refactor the entire frontend to look like meow
1. Unit testing for front end functions and backend
1. frontend confusing variable and function names
1. test that url stuff works ?query=125!@#$%^&()

## Small things
1. Improve docker file
2. add .dockerignore ✓
3. add deploy script
4. Search bar + search button style ✓
3. Sometimes "Loading.." does not show up ✓
1. When you have something searched and you switch sections, it doesn't re issue a query ✓
1. When you paste a link into the browser with a query, it doesn't fill in the search text field with the query from the url
1. Clear section filtering 
1. Don't have 2 sources of truth for section (url and useState in App.js)
1. Massive housekeeping of App.js:
  1. Keyboard shortcuts have 2 places of duplicate code
  1. put helper functions outside
1. Actually make the radio buttons update according to redux state LOL