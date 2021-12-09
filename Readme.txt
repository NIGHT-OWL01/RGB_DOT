Hi, i am Ganesh

I tried to make this webapp('base') as per mentioned in documents


*About Project:

as per docs for Farmer to own None,one or many tractors i created 'foreignkey' in tractor model.
For Each Tractor to have multiple implements and implements are limited i used 'MultiSelectField' in tractor model.

1. A form is created to add detail about new tractor record ('Add Tractor' link)
/* i used class based view and extended genericView 'CreateView' for tractor create form,
all fields except owner are shown on form, owner is assigned during form submission,
i overrided form_valid() method to assign current user to tractor.
*/

2. A page with list of all the tractor records present are on 'All Tractor List' link
/* generic listView is used for list of tractors */

3. Tractor details are available on 'All Tractor List' link click on tractor name to get name of owner
/*generic DetailView is used for details of tractor */

Sorry for delay