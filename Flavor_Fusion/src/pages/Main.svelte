<script>
    import CountrySelection from "../components/countrySelection.svelte";
    import FoodTypes from "../components/foodTypes.svelte";   
    const homepage_bg  = "images/world_map.png"
    const Extra_filters  = ["Vegan", "Carnivore", "Vegeterian", "Keto", "Mediterrean", "Halal"

    ]

    
    

</script>


<main class="flex flex-col flex-1 p-4">
    
    <section id="homepage" class="grid grid-cols-1 1g:grid-cols-2 gap-8 py-4 sm:py-2">
        
        <div class="flex flex-col lg:justify-center text-center lg:text-left gap-3 md:gap-8 lg:gap-10">
            
            <h2 class="text-2xl sm:text-4xl md:text-6xl">
                Not sure where to start?
            </h2>
        </div>
        <div class="m-0">
            
            <label for="country"
            class="display: inline-block jacques-francois-shadow-regular float-left px-10 pb-0 pt-5 text-2xl"> 
                Country
            </label>
            
           <label for="Food_type" 
            class="display: inline-block jacques-francois-shadow-regular float-right px-10 pb-0 pt-5 text-2xl"> 
                Type of Food
            </label>
            <br>
            <br>
            <br>

            <form>

            <div class="m-0 py-0 px-8 float-left ">
                <CountrySelection/>
            </div>

            <div class="m-0 py-0 px-8 float-right">
                <FoodTypes/>
            </div>

            <label for="Extra_filters" ></label>

        </form>

        </div>     
        
    </section>

</main>