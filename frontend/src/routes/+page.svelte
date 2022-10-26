<script>
    async function loadPosts() {
		const res = await fetch('http://localhost:8000/api/v1/demo/posts');
        console.log(res.ok)
        
		if (res.ok) {
			const data = await res.json();

            console.log(data)
			return data;
		}

		const { message } = await res.json();

		return {
			error: new Error(message)
		};
	};
</script> 


<div>
    <h1 class="text-3xl font-bold underline mb-6">
        Blog Posts
    </h1>

    {#await loadPosts()}
    ...
    {:then posts}
        {#each posts as post}
            <h1>{post.title}</h1>
            <h4>Publish date: {post.date}</h4>
            <p>{post.text}</p>
        {/each}
    {/await}
</div>