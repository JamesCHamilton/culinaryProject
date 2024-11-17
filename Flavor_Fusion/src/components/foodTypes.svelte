<script>
const Type_of_Foods  = ["Soup", "Pasta", "Pizza", "Salads", "Curry", "Pies/Pastries", "Bread/Doughs", "Stew/Hotpots",
        "Cake/Baking", "Sauces", "Drinks", "Sandwiches", "Sushi", "Rice Dishes"
    ]
</script>


<!--Button-->
<select name="Type_of_Food" id="Food_type" required
class="text-black  bg-white hover:bg-grey focus:ring-4 focus:outline-black focus:ring-black font-medium rounded-lg text-sm px-20 py-2.5 text-center inline-flex items-center dark:bg-slate-200 hover:bg-gray-200 dark:focus:ring-black">
    
    <option value="" disabled selected>Select a Food Type</option>
    
    {#each Type_of_Foods as Type_of_Food}
    <option value={Type_of_Food}>   {Type_of_Food}  </option>
    {/each}

</select>