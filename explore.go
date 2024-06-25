	// Create and seed the generator.
	// Typically a non-fixed seed should be used, such as time.Now().UnixNano().
	// Using a fixed seed will produce the same output on every run.
	r := rand.New(rand.NewSource(99))



	// Seed the random number generator with a given seed.
	func seedRandomNumberGenerator(seed int64) *rand.Rand {
		return rand.New(rand.NewSource(seed))
	}

	// Usage:
	r := seedRandomNumberGenerator(99)

	
