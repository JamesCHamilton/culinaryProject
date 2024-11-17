<script lang="ts">
    const logo: string = "images/logo.png"
    export let y;
    const headerTabs = [
        {name: "Find a recipe", link: "#Finder"},
        {name: "Share your recipe", link: "#Sharer"},
        {name: "Ingredients Near You", link: "#NearYou"}
    ]
</script>


<header class={"sticky z-[10] top-0 duration-200 px-0 mx-0 flex items-center justify-between w-screen" + (
    y + 0 ? "py-4 bg-slate-950" : "py-6 bg-transparent border-transparent"
)}>
    <div class="bg-black sm:flex items-center gap-10 hidden w-screen px-0 mx-0">

        <img src={logo} alt="Main Logo" class="object-cover z-[2] max-h-[10vh] top-0 left-0"/>

        <b1 class="font-bold poppins text-white top-0 ">Flavor Fusion</b1>

        <div class= "sm:flex items-center gap-4 hidden">
            {#each headerTabs as headerTab}
                <a href={headerTab.link} class="duration-200 hover:text-white-400">
                    <p1 class= "text-white font-jacques-francois-shadow-regular">{headerTab.name}</p1>
                </a>
            {/each}
        </div>

    </div>
        
      
</header>