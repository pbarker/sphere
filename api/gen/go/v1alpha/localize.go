package sphere_api_v1alpha

import (
	"gorgonia.org/tensor"
)

// Dense will convert a remotely defined tensor to a local gorgonia dense tensor.
func (t *Tensor) Dense() *tensor.Dense {
	shape := []int{}
	for _, i := range t.GetShape() {
		shape = append(shape, int(i))
	}
	tens := tensor.New(tensor.WithShape(shape...), tensor.WithBacking(t.Data))
	return tens
}
