<script context="module">
	// see https://kit.svelte.dev/docs#loading
	export async function load({ fetch }) {
		const res = await fetch('http://backend:8000/api/v1/demo/posts');

		if (res.ok) {
			const data = await res.json();
            const posts = data

			return {
				props: { posts }
			};
		}

		const { message } = await res.json();

		return {
			error: new Error(message)
		};
	};
</script>


<script>
    export let posts;

	function handleOnSubmit() {
		console.log("I'm the handleOnSubmit() in App.svelte")
	}
</script> 


<div>
    {#each posts as post}
		<h1>{post.title}</h1>
		<h4>Publish date: {post.date}</h4>
		<p>{post.text}</p>
	{/each}

	<div>
		<form on:submit={handleOnSubmit}>
			<input type="text" name="username" id="">
			<input type="text" name="password" id="">
			<input type="button">
		</form>
	</div>
</div>