<script>
    import Nav from '$lib/components/Nav.svelte';

    import "../app.css";
</script>

<main>
    <Nav />

    <div class="container">
        <slot class="container" />
    </div>
</main>


<style>
    main{
        margin: auto;
        font-family: 'Noto Sans JP', sans-serif;
    }

    .container{
        max-width: 600px;
        margin: auto;
    }

</style>