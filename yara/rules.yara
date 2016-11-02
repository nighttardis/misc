rule HelloWorld
{
	strings:
		$a = "Hello world"

	condition:
		$a
}
