package main


import (
	"github.com/pili-engineering/pili-sdk-go/pili"
	"fmt"
)

const (
    ACCESS_KEY = "U_vrtWYXXafFOFgZjPsTtiOh0t5AZF0RAhqyq7DL"
    SECRET_KEY = "q4TLb5HvlO4sQeHLktnSzWy6rYw2YSiuFFGQ6nwn"
    HUB_NAME   = "10minute"   // The Hub must be exists before use
)

func main() {
	credentials := pili.NewCredentials(ACCESS_KEY, SECRET_KEY)
    hub := pili.NewHub(credentials, HUB_NAME)


    options := pili.OptionalArguments{               // optional
	    Title:           "", // optional, auto-generated as default
	    PublishKey:      "",        // optional, auto-generated as default
	    PublishSecurity: "",                  // optional, can be "dynamic" or "static", "dynamic" as default
	}
	stream, err := hub.CreateStream(options)
	if err != nil {
	    fmt.Println("Error:", err)
	}
	fmt.Println("CreateStream:\n", stream)

	//生成stream Publishurl
	url := stream.RtmpPublishUrl()
	fmt.Println("Stream RtmpPublishUrl:\n", url)

	//生成streamJson
	streamJson, err := stream.ToJSONString()
	if err != nil {
    fmt.Println("Error:", err)
	}
	fmt.Println("Stream ToJSONString:\n", streamJson)
}

