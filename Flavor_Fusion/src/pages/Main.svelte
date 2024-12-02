<script>
    import CountrySelection from "../components/countrySelection.svelte";
    import FoodTypes from "../components/foodTypes.svelte"; 
    import ExtraFilters from "../components/ExtraFilters.svelte"; 
    const homepage_bg  = "images/world_map.png"
</script>


<main class="flex flex-col flex-auto p-4" >
    
    <section id="homepage" class="grid grid-cols-1 1g:grid-cols-2 gap-8 sm:py-2"
    >

        <div class="flex flex-col lg:justify-center text-center lg:text-left gap-3 md:gap-8 lg:gap-10">
            
            <h2 class="text-2xl sm:text-4xl md:text-6xl">
                Not sure where to start?
            </h2>
        </div>

        <!--There are three fields that will be processed in JS backend, that will determine the next next page loaded-->
        <form 
        class="m-0"
        action="/submit-form"
        method="POST"
        >
            <!--Countries-->
            <div>
                <label for="country"
                class="display: inline-block jacques-francois-shadow-regular float-left pb-0 pt-5 text-2xl"> 
                    Country
                    <br>
                    <div class="m-0 py-0 float-left">
                        <CountrySelection/>
                    </div>
                </label>
            </div>
            
            <!--Food Types-->
            <div>
                <label for="Food_type" 
                    class="display: inline-block jacques-francois-shadow-regular float-right pb-0 pt-5 text-2xl"> 
                        Type of Food
                        <br>
                        <div class="m-0 py-0 float-right">
                            <FoodTypes/>
                        </div>
                    </label>
            </div>
            
            <br><br><br><br><br>

            <!--Extra Filters-->
            <div class="flex items-center justify-center">
                <label for="Extra_Filters"
                class="display: inline-block jacques-francois-shadow-regular text-2xl"
                >
                    Extra Filters
                    <br>
                    <div class="m-0 py-0">
                        <ExtraFilters/>
                    </div>
                </label>
            </div>

            <!--Submit Button-->
            <div class="flex items-center justify-center mt-8">
                <button 
                    type="submit"
                    class="jacques-francois-shadow-regular px-6 py-2 bg-slate-500 text-white text-xl font-semibold rounded hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300"
                >
                    Submit
                </button>
            </div>


        </form>     
        <!--Finsih footer-->
    </section>

</main>