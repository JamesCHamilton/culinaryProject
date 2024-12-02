<script>
    const Extra_filters  = ["Vegan", "Carnivore", "Vegeterian", "Keto", "Mediterrean", "Halal"
        ]
</script>

<!--Button-->
<select name="Extra_filter" id="Extra_filter"
class="text-black  bg-white hover:bg-grey focus:ring-4 focus:outline-black focus:ring-black font-medium rounded-lg text-sm px-20 py-2.5 text-center inline-flex items-center dark:bg-slate-200 hover:bg-gray-200 dark:focus:ring-black">
    
    <option value="" disabled selected>Select a Food Type</option>
    
    {#each Extra_filters as Extra_filter}
    <option value={Extra_filter}>   {Extra_filter}  </option>
    {/each}

</select>