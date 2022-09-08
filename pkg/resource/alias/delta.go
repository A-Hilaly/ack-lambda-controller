// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License"). You may
// not use this file except in compliance with the License. A copy of the
// License is located at
//
//     http://aws.amazon.com/apache2.0/
//
// or in the "license" file accompanying this file. This file is distributed
// on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
// express or implied. See the License for the specific language governing
// permissions and limitations under the License.

// Code generated by ack-generate. DO NOT EDIT.

package alias

import (
	"bytes"
	"reflect"

	ackcompare "github.com/aws-controllers-k8s/runtime/pkg/compare"
)

// Hack to avoid import errors during build...
var (
	_ = &bytes.Buffer{}
	_ = &reflect.Method{}
)

// newResourceDelta returns a new `ackcompare.Delta` used to compare two
// resources
func newResourceDelta(
	a *resource,
	b *resource,
) *ackcompare.Delta {
	delta := ackcompare.NewDelta()
	if (a == nil && b != nil) ||
		(a != nil && b == nil) {
		delta.Add("", a, b)
		return delta
	}

	if ackcompare.HasNilDifference(a.ko.Spec.Description, b.ko.Spec.Description) {
		delta.Add("Spec.Description", a.ko.Spec.Description, b.ko.Spec.Description)
	} else if a.ko.Spec.Description != nil && b.ko.Spec.Description != nil {
		if *a.ko.Spec.Description != *b.ko.Spec.Description {
			delta.Add("Spec.Description", a.ko.Spec.Description, b.ko.Spec.Description)
		}
	}
	if ackcompare.HasNilDifference(a.ko.Spec.FunctionName, b.ko.Spec.FunctionName) {
		delta.Add("Spec.FunctionName", a.ko.Spec.FunctionName, b.ko.Spec.FunctionName)
	} else if a.ko.Spec.FunctionName != nil && b.ko.Spec.FunctionName != nil {
		if *a.ko.Spec.FunctionName != *b.ko.Spec.FunctionName {
			delta.Add("Spec.FunctionName", a.ko.Spec.FunctionName, b.ko.Spec.FunctionName)
		}
	}
	if !reflect.DeepEqual(a.ko.Spec.FunctionRef, b.ko.Spec.FunctionRef) {
		delta.Add("Spec.FunctionRef", a.ko.Spec.FunctionRef, b.ko.Spec.FunctionRef)
	}
	if ackcompare.HasNilDifference(a.ko.Spec.FunctionVersion, b.ko.Spec.FunctionVersion) {
		delta.Add("Spec.FunctionVersion", a.ko.Spec.FunctionVersion, b.ko.Spec.FunctionVersion)
	} else if a.ko.Spec.FunctionVersion != nil && b.ko.Spec.FunctionVersion != nil {
		if *a.ko.Spec.FunctionVersion != *b.ko.Spec.FunctionVersion {
			delta.Add("Spec.FunctionVersion", a.ko.Spec.FunctionVersion, b.ko.Spec.FunctionVersion)
		}
	}
	if ackcompare.HasNilDifference(a.ko.Spec.Name, b.ko.Spec.Name) {
		delta.Add("Spec.Name", a.ko.Spec.Name, b.ko.Spec.Name)
	} else if a.ko.Spec.Name != nil && b.ko.Spec.Name != nil {
		if *a.ko.Spec.Name != *b.ko.Spec.Name {
			delta.Add("Spec.Name", a.ko.Spec.Name, b.ko.Spec.Name)
		}
	}
	if ackcompare.HasNilDifference(a.ko.Spec.RoutingConfig, b.ko.Spec.RoutingConfig) {
		delta.Add("Spec.RoutingConfig", a.ko.Spec.RoutingConfig, b.ko.Spec.RoutingConfig)
	} else if a.ko.Spec.RoutingConfig != nil && b.ko.Spec.RoutingConfig != nil {
		if ackcompare.HasNilDifference(a.ko.Spec.RoutingConfig.AdditionalVersionWeights, b.ko.Spec.RoutingConfig.AdditionalVersionWeights) {
			delta.Add("Spec.RoutingConfig.AdditionalVersionWeights", a.ko.Spec.RoutingConfig.AdditionalVersionWeights, b.ko.Spec.RoutingConfig.AdditionalVersionWeights)
		} else if a.ko.Spec.RoutingConfig.AdditionalVersionWeights != nil && b.ko.Spec.RoutingConfig.AdditionalVersionWeights != nil {
			if !reflect.DeepEqual(a.ko.Spec.RoutingConfig.AdditionalVersionWeights, b.ko.Spec.RoutingConfig.AdditionalVersionWeights) {
				delta.Add("Spec.RoutingConfig.AdditionalVersionWeights", a.ko.Spec.RoutingConfig.AdditionalVersionWeights, b.ko.Spec.RoutingConfig.AdditionalVersionWeights)
			}
		}
	}

	return delta
}
